# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Exact3NumericText
from . import GenericIdentification1
from . import Max70Text
from . import PlainCardData1

class PaymentCard4(base_types._BaseFieldType):

	__slots__ = ["_AddtlCardData", "_CardBrnd", "_CardCtryCd", "_PlainCardData"]
	@property
	def AddtlCardData(self):
		return self._AddtlCardData

	@AddtlCardData.setter
	def AddtlCardData(self, value):
		self._AddtlCardData = value if value is not None else base_types.UninitialisedField(self, 'AddtlCardData', Max70Text, False)

	@AddtlCardData.deleter
	def AddtlCardData(self):
		del self._AddtlCardData
		self._AddtlCardData = base_types.UninitialisedField(self, 'AddtlCardData', Max70Text, False)

	@property
	def CardBrnd(self):
		return self._CardBrnd

	@CardBrnd.setter
	def CardBrnd(self, value):
		self._CardBrnd = value if value is not None else base_types.UninitialisedField(self, 'CardBrnd', GenericIdentification1, False)

	@CardBrnd.deleter
	def CardBrnd(self):
		del self._CardBrnd
		self._CardBrnd = base_types.UninitialisedField(self, 'CardBrnd', GenericIdentification1, False)

	@property
	def CardCtryCd(self):
		return self._CardCtryCd

	@CardCtryCd.setter
	def CardCtryCd(self, value):
		self._CardCtryCd = value if value is not None else base_types.UninitialisedField(self, 'CardCtryCd', Exact3NumericText, False)

	@CardCtryCd.deleter
	def CardCtryCd(self):
		del self._CardCtryCd
		self._CardCtryCd = base_types.UninitialisedField(self, 'CardCtryCd', Exact3NumericText, False)

	@property
	def PlainCardData(self):
		return self._PlainCardData

	@PlainCardData.setter
	def PlainCardData(self, value):
		self._PlainCardData = value if value is not None else base_types.UninitialisedField(self, 'PlainCardData', PlainCardData1, False)

	@PlainCardData.deleter
	def PlainCardData(self):
		del self._PlainCardData
		self._PlainCardData = base_types.UninitialisedField(self, 'PlainCardData', PlainCardData1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlCardData', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardBrnd', type=GenericIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardCtryCd', type=Exact3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlainCardData', type=PlainCardData1, min=0, max=1, mutex_group=None, array=False),
	))