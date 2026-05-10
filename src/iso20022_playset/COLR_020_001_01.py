import base_types
import TripartyCollateralTransactionInstructionProcessingStatusAdviceV01

class COLR_020_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_TrptyCollTxInstrPrcgStsAdvc"]
		@property
		def TrptyCollTxInstrPrcgStsAdvc(self):
			return self._TrptyCollTxInstrPrcgStsAdvc

		@TrptyCollTxInstrPrcgStsAdvc.setter
		def TrptyCollTxInstrPrcgStsAdvc(self, value):
			self._TrptyCollTxInstrPrcgStsAdvc = value if type(value) != auto else self.make_default("TrptyCollTxInstrPrcgStsAdvc")

		@TrptyCollTxInstrPrcgStsAdvc.deleter
		def TrptyCollTxInstrPrcgStsAdvc(self):
			del self._TrptyCollTxInstrPrcgStsAdvc
			self._TrptyCollTxInstrPrcgStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='TrptyCollTxInstrPrcgStsAdvc', type=TripartyCollateralTransactionInstructionProcessingStatusAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))

