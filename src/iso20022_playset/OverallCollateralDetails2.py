import base_types
import CollateralAmount15
import CollateralStatus1Code
import DateAndDateTime2Choice
import PercentageRate
import Max350Text

class OverallCollateralDetails2(base_types._BaseFieldType):

	__slots__ = ["_CollAddtlDtls", "_GblCollSts", "_ValtnDt", "_ValtnAmts", "_MrgnRate"]
	@property
	def CollAddtlDtls(self):
		return self._CollAddtlDtls

	@CollAddtlDtls.setter
	def CollAddtlDtls(self, value):
		self._CollAddtlDtls = value if type(value) != auto else self.make_default("CollAddtlDtls")

	@CollAddtlDtls.deleter
	def CollAddtlDtls(self):
		del self._CollAddtlDtls
		self._CollAddtlDtls = None

	@property
	def GblCollSts(self):
		return self._GblCollSts

	@GblCollSts.setter
	def GblCollSts(self, value):
		self._GblCollSts = value if type(value) != auto else self.make_default("GblCollSts")

	@GblCollSts.deleter
	def GblCollSts(self):
		del self._GblCollSts
		self._GblCollSts = None

	@property
	def ValtnDt(self):
		return self._ValtnDt

	@ValtnDt.setter
	def ValtnDt(self, value):
		self._ValtnDt = value if type(value) != auto else self.make_default("ValtnDt")

	@ValtnDt.deleter
	def ValtnDt(self):
		del self._ValtnDt
		self._ValtnDt = None

	@property
	def ValtnAmts(self):
		return self._ValtnAmts

	@ValtnAmts.setter
	def ValtnAmts(self, value):
		self._ValtnAmts = value if type(value) != auto else self.make_default("ValtnAmts")

	@ValtnAmts.deleter
	def ValtnAmts(self):
		del self._ValtnAmts
		self._ValtnAmts = None

	@property
	def MrgnRate(self):
		return self._MrgnRate

	@MrgnRate.setter
	def MrgnRate(self, value):
		self._MrgnRate = value if type(value) != auto else self.make_default("MrgnRate")

	@MrgnRate.deleter
	def MrgnRate(self):
		del self._MrgnRate
		self._MrgnRate = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollAddtlDtls', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GblCollSts', type=CollateralStatus1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnDt', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnAmts', type=CollateralAmount15, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
	))

