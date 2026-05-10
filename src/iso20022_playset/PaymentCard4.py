from . import base_types
import GenericIdentification1
import Max70Text
import Exact3NumericText
import PlainCardData1

class PaymentCard4(base_types._BaseFieldType):

	__slots__ = ["_CardBrnd", "_PlainCardData", "_CardCtryCd", "_AddtlCardData"]
	@property
	def CardBrnd(self):
		return self._CardBrnd

	@CardBrnd.setter
	def CardBrnd(self, value):
		self._CardBrnd = value if type(value) != auto else self.make_default("CardBrnd")

	@CardBrnd.deleter
	def CardBrnd(self):
		del self._CardBrnd
		self._CardBrnd = None

	@property
	def PlainCardData(self):
		return self._PlainCardData

	@PlainCardData.setter
	def PlainCardData(self, value):
		self._PlainCardData = value if type(value) != auto else self.make_default("PlainCardData")

	@PlainCardData.deleter
	def PlainCardData(self):
		del self._PlainCardData
		self._PlainCardData = None

	@property
	def CardCtryCd(self):
		return self._CardCtryCd

	@CardCtryCd.setter
	def CardCtryCd(self, value):
		self._CardCtryCd = value if type(value) != auto else self.make_default("CardCtryCd")

	@CardCtryCd.deleter
	def CardCtryCd(self):
		del self._CardCtryCd
		self._CardCtryCd = None

	@property
	def AddtlCardData(self):
		return self._AddtlCardData

	@AddtlCardData.setter
	def AddtlCardData(self, value):
		self._AddtlCardData = value if type(value) != auto else self.make_default("AddtlCardData")

	@AddtlCardData.deleter
	def AddtlCardData(self):
		del self._AddtlCardData
		self._AddtlCardData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CardBrnd', type=GenericIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlainCardData', type=PlainCardData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardCtryCd', type=Exact3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlCardData', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
	))

