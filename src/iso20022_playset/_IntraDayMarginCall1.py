# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import GenericIdentification165
from . import ISODateTime

class IntraDayMarginCall1(base_types._BaseFieldType):

	__slots__ = ["_IntraDayCall", "_MrgnAcctId", "_TmStmp"]
	@property
	def IntraDayCall(self):
		return self._IntraDayCall

	@IntraDayCall.setter
	def IntraDayCall(self, value):
		self._IntraDayCall = value if value is not None else base_types.UninitialisedField(self, 'IntraDayCall', ActiveCurrencyAndAmount, False)

	@IntraDayCall.deleter
	def IntraDayCall(self):
		del self._IntraDayCall
		self._IntraDayCall = base_types.UninitialisedField(self, 'IntraDayCall', ActiveCurrencyAndAmount, False)

	@property
	def MrgnAcctId(self):
		return self._MrgnAcctId

	@MrgnAcctId.setter
	def MrgnAcctId(self, value):
		self._MrgnAcctId = value if value is not None else base_types.UninitialisedField(self, 'MrgnAcctId', GenericIdentification165, False)

	@MrgnAcctId.deleter
	def MrgnAcctId(self):
		del self._MrgnAcctId
		self._MrgnAcctId = base_types.UninitialisedField(self, 'MrgnAcctId', GenericIdentification165, False)

	@property
	def TmStmp(self):
		return self._TmStmp

	@TmStmp.setter
	def TmStmp(self, value):
		self._TmStmp = value if value is not None else base_types.UninitialisedField(self, 'TmStmp', ISODateTime, False)

	@TmStmp.deleter
	def TmStmp(self):
		del self._TmStmp
		self._TmStmp = base_types.UninitialisedField(self, 'TmStmp', ISODateTime, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='IntraDayCall', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnAcctId', type=GenericIdentification165, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TmStmp', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
	))