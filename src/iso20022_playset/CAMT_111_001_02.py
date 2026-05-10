import base_types
import InvestigationResponseV02

class CAMT_111_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_InvstgtnRspn"]
		@property
		def InvstgtnRspn(self):
			return self._InvstgtnRspn

		@InvstgtnRspn.setter
		def InvstgtnRspn(self, value):
			self._InvstgtnRspn = value if type(value) != auto else self.make_default("InvstgtnRspn")

		@InvstgtnRspn.deleter
		def InvstgtnRspn(self):
			del self._InvstgtnRspn
			self._InvstgtnRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='InvstgtnRspn', type=InvestigationResponseV02, min=1, max=1, mutex_group=None, array=False),
		))

