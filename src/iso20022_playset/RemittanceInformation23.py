import base_types
import Max35Text
import Max140Text
import StructuredRemittanceInformation18
import OriginalPaymentInformation10

class RemittanceInformation23(base_types._BaseFieldType):

	__slots__ = ["_RmtId", "_Strd", "_Ustrd", "_OrgnlPmtInf"]
	@property
	def RmtId(self):
		return self._RmtId

	@RmtId.setter
	def RmtId(self, value):
		self._RmtId = value if type(value) != auto else self.make_default("RmtId")

	@RmtId.deleter
	def RmtId(self):
		del self._RmtId
		self._RmtId = None

	@property
	def Strd(self):
		return self._Strd

	@Strd.setter
	def Strd(self, value):
		self._Strd = value if type(value) != auto else self.make_default("Strd")

	@Strd.deleter
	def Strd(self):
		del self._Strd
		self._Strd = None

	@property
	def Ustrd(self):
		return self._Ustrd

	@Ustrd.setter
	def Ustrd(self, value):
		self._Ustrd = value if type(value) != auto else self.make_default("Ustrd")

	@Ustrd.deleter
	def Ustrd(self):
		del self._Ustrd
		self._Ustrd = None

	@property
	def OrgnlPmtInf(self):
		return self._OrgnlPmtInf

	@OrgnlPmtInf.setter
	def OrgnlPmtInf(self, value):
		self._OrgnlPmtInf = value if type(value) != auto else self.make_default("OrgnlPmtInf")

	@OrgnlPmtInf.deleter
	def OrgnlPmtInf(self):
		del self._OrgnlPmtInf
		self._OrgnlPmtInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RmtId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Strd', type=StructuredRemittanceInformation18, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ustrd', type=Max140Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlPmtInf', type=OriginalPaymentInformation10, min=1, max=1, mutex_group=None, array=False),
	))

