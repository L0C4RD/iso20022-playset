import base_types
import SecuritiesFinancingConfirmation002V11

class SESE_035_002_11():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesFincgConf"]
		@property
		def SctiesFincgConf(self):
			return self._SctiesFincgConf

		@SctiesFincgConf.setter
		def SctiesFincgConf(self, value):
			self._SctiesFincgConf = value if type(value) != auto else self.make_default("SctiesFincgConf")

		@SctiesFincgConf.deleter
		def SctiesFincgConf(self):
			del self._SctiesFincgConf
			self._SctiesFincgConf = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesFincgConf', type=SecuritiesFinancingConfirmation002V11, min=1, max=1, mutex_group=None, array=False),
		))

