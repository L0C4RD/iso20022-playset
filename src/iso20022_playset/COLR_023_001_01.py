from . import base_types
import TripartyCollateralStatusAdviceV01

class COLR_023_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_TrptyCollStsAdvc"]
		@property
		def TrptyCollStsAdvc(self):
			return self._TrptyCollStsAdvc

		@TrptyCollStsAdvc.setter
		def TrptyCollStsAdvc(self, value):
			self._TrptyCollStsAdvc = value if type(value) != auto else self.make_default("TrptyCollStsAdvc")

		@TrptyCollStsAdvc.deleter
		def TrptyCollStsAdvc(self):
			del self._TrptyCollStsAdvc
			self._TrptyCollStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='TrptyCollStsAdvc', type=TripartyCollateralStatusAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))

