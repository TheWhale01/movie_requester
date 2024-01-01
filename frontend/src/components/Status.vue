<template>
	<span :class="class">{{ str }}</span>
</template>
<script lang="ts">
import StatusType from '@/interfaces/status_type.enum';

export default {
	props: {
		statusProps: {type: Number, required: true},
	},

	data() {
		return {
			str: '' as string,
			class: '' as string,
			status: -1 as number,
		};
	},

	watch: {
		statusProps: function(newStatus, oldStatus) {
			this.status = newStatus;
			this.$forceUpdate();
		},
	},

	mounted(): void { this.getStatus(); },
	updated(): void { this.getStatus(); },

	methods: {
		getStatus(): void {
			this.status = this.statusProps
			switch (this.status) {
				case StatusType.PENDING:
					this.str = 'Pending';
					break ;
				case StatusType.ACCEPTED:
					this.str = 'Accepted';
					break ;
				case StatusType.REFUSED:
					this.str = 'Refused';
					break ;
				case StatusType.FINISHED:
					this.str = 'Finished';
					break ;
				default:
					this.str = 'Pending';
					break;
			}
			this.class = this.str.toLowerCase();
		}
	}
}
</script>
<style scoped>

span {
	padding: 10px;
	border-radius: 10px;
}

.pending {
	background-color: #5046e5;
}

.accepted {
	background-color: green;
}

.refused {
	background-color: red;
}

.finished {
	background-color: #ffcc3f;
}
</style>