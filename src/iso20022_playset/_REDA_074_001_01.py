from . import base_types
from ._TripartyCollateralUnilateralRemovalRequestV01 import TripartyCollateralUnilateralRemovalRequestV01

class REDA_074_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_TrptyCollUnltrlRmvlReq"]
		@property
		def TrptyCollUnltrlRmvlReq(self):
			return self._TrptyCollUnltrlRmvlReq

		@TrptyCollUnltrlRmvlReq.setter
		def TrptyCollUnltrlRmvlReq(self, value):
			self._TrptyCollUnltrlRmvlReq = value if type(value) != base_types.auto else self.make_default("TrptyCollUnltrlRmvlReq")

		@TrptyCollUnltrlRmvlReq.deleter
		def TrptyCollUnltrlRmvlReq(self):
			del self._TrptyCollUnltrlRmvlReq
			self._TrptyCollUnltrlRmvlReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='TrptyCollUnltrlRmvlReq', type=TripartyCollateralUnilateralRemovalRequestV01, min=1, max=1, mutex_group=None, array=False),
		))

