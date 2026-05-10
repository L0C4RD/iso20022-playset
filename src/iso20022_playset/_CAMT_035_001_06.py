from . import base_types
from ._ProprietaryFormatInvestigationV06 import ProprietaryFormatInvestigationV06

class CAMT_035_001_06():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_PrtryFrmtInvstgtn"]
		@property
		def PrtryFrmtInvstgtn(self):
			return self._PrtryFrmtInvstgtn

		@PrtryFrmtInvstgtn.setter
		def PrtryFrmtInvstgtn(self, value):
			self._PrtryFrmtInvstgtn = value if type(value) != base_types.auto else self.make_default("PrtryFrmtInvstgtn")

		@PrtryFrmtInvstgtn.deleter
		def PrtryFrmtInvstgtn(self):
			del self._PrtryFrmtInvstgtn
			self._PrtryFrmtInvstgtn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='PrtryFrmtInvstgtn', type=ProprietaryFormatInvestigationV06, min=1, max=1, mutex_group=None, array=False),
		))

