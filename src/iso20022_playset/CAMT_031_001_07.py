import base_types
import RejectInvestigationV07

class CAMT_031_001_07():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_RjctInvstgtn"]
		@property
		def RjctInvstgtn(self):
			return self._RjctInvstgtn

		@RjctInvstgtn.setter
		def RjctInvstgtn(self, value):
			self._RjctInvstgtn = value if type(value) != auto else self.make_default("RjctInvstgtn")

		@RjctInvstgtn.deleter
		def RjctInvstgtn(self):
			del self._RjctInvstgtn
			self._RjctInvstgtn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RjctInvstgtn', type=RejectInvestigationV07, min=1, max=1, mutex_group=None, array=False),
		))

