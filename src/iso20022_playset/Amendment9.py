from . import base_types
import UndertakingAmendmentResponseMessage1

class Amendment9(base_types._BaseFieldType):

	__slots__ = ["_UdrtkgAmdmntRspnMsg"]
	@property
	def UdrtkgAmdmntRspnMsg(self):
		return self._UdrtkgAmdmntRspnMsg

	@UdrtkgAmdmntRspnMsg.setter
	def UdrtkgAmdmntRspnMsg(self, value):
		self._UdrtkgAmdmntRspnMsg = value if type(value) != auto else self.make_default("UdrtkgAmdmntRspnMsg")

	@UdrtkgAmdmntRspnMsg.deleter
	def UdrtkgAmdmntRspnMsg(self):
		del self._UdrtkgAmdmntRspnMsg
		self._UdrtkgAmdmntRspnMsg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='UdrtkgAmdmntRspnMsg', type=UndertakingAmendmentResponseMessage1, min=1, max=1, mutex_group=None, array=False),
	))

