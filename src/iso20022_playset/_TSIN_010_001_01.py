from . import base_types
from ._PartyRegistrationAndGuaranteeStatusV01 import PartyRegistrationAndGuaranteeStatusV01

class TSIN_010_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_PtyRegnAndGrntSts"]
		@property
		def PtyRegnAndGrntSts(self):
			return self._PtyRegnAndGrntSts

		@PtyRegnAndGrntSts.setter
		def PtyRegnAndGrntSts(self, value):
			self._PtyRegnAndGrntSts = value if type(value) != base_types.auto else self.make_default("PtyRegnAndGrntSts")

		@PtyRegnAndGrntSts.deleter
		def PtyRegnAndGrntSts(self):
			del self._PtyRegnAndGrntSts
			self._PtyRegnAndGrntSts = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='PtyRegnAndGrntSts', type=PartyRegistrationAndGuaranteeStatusV01, min=1, max=1, mutex_group=None, array=False),
		))

