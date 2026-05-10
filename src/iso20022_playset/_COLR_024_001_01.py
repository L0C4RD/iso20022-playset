from . import base_types
from ._TripartyCollateralAllegementNotificationCancellationAdviceV01 import TripartyCollateralAllegementNotificationCancellationAdviceV01

class COLR_024_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_TrptyCollAllgmtNtfctnCxlAdvc"]
		@property
		def TrptyCollAllgmtNtfctnCxlAdvc(self):
			return self._TrptyCollAllgmtNtfctnCxlAdvc

		@TrptyCollAllgmtNtfctnCxlAdvc.setter
		def TrptyCollAllgmtNtfctnCxlAdvc(self, value):
			self._TrptyCollAllgmtNtfctnCxlAdvc = value if type(value) != base_types.auto else self.make_default("TrptyCollAllgmtNtfctnCxlAdvc")

		@TrptyCollAllgmtNtfctnCxlAdvc.deleter
		def TrptyCollAllgmtNtfctnCxlAdvc(self):
			del self._TrptyCollAllgmtNtfctnCxlAdvc
			self._TrptyCollAllgmtNtfctnCxlAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='TrptyCollAllgmtNtfctnCxlAdvc', type=TripartyCollateralAllegementNotificationCancellationAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))

