from . import base_types
import ReturnGeneralBusinessInformationV06

class CAMT_021_001_06():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_RtrGnlBizInf"]
		@property
		def RtrGnlBizInf(self):
			return self._RtrGnlBizInf

		@RtrGnlBizInf.setter
		def RtrGnlBizInf(self, value):
			self._RtrGnlBizInf = value if type(value) != auto else self.make_default("RtrGnlBizInf")

		@RtrGnlBizInf.deleter
		def RtrGnlBizInf(self):
			del self._RtrGnlBizInf
			self._RtrGnlBizInf = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RtrGnlBizInf', type=ReturnGeneralBusinessInformationV06, min=1, max=1, mutex_group=None, array=False),
		))

