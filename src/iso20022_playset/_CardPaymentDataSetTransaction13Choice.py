# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CardPaymentDataSetTransaction50
from . import CardPaymentDataSetTransaction51
from . import CardPaymentDataSetTransaction52
from . import CardPaymentDataSetTransaction53
from . import TokenRequestComponent5

class CardPaymentDataSetTransaction13Choice(base_types._BaseFieldType):

	__slots__ = ["_AuthstnReq", "_AuthstnRspn", "_Cmpltn", "_Cxl", "_TknReq", "_TknRspn"]
	@property
	def AuthstnReq(self):
		return self._AuthstnReq

	@AuthstnReq.setter
	def AuthstnReq(self, value):
		self._AuthstnReq = value if value is not None else base_types.UninitialisedField(self, 'AuthstnReq', CardPaymentDataSetTransaction52, False)

	@AuthstnReq.deleter
	def AuthstnReq(self):
		del self._AuthstnReq
		self._AuthstnReq = base_types.UninitialisedField(self, 'AuthstnReq', CardPaymentDataSetTransaction52, False)

	@property
	def AuthstnRspn(self):
		return self._AuthstnRspn

	@AuthstnRspn.setter
	def AuthstnRspn(self, value):
		self._AuthstnRspn = value if value is not None else base_types.UninitialisedField(self, 'AuthstnRspn', CardPaymentDataSetTransaction53, False)

	@AuthstnRspn.deleter
	def AuthstnRspn(self):
		del self._AuthstnRspn
		self._AuthstnRspn = base_types.UninitialisedField(self, 'AuthstnRspn', CardPaymentDataSetTransaction53, False)

	@property
	def Cmpltn(self):
		return self._Cmpltn

	@Cmpltn.setter
	def Cmpltn(self, value):
		self._Cmpltn = value if value is not None else base_types.UninitialisedField(self, 'Cmpltn', CardPaymentDataSetTransaction51, False)

	@Cmpltn.deleter
	def Cmpltn(self):
		del self._Cmpltn
		self._Cmpltn = base_types.UninitialisedField(self, 'Cmpltn', CardPaymentDataSetTransaction51, False)

	@property
	def Cxl(self):
		return self._Cxl

	@Cxl.setter
	def Cxl(self, value):
		self._Cxl = value if value is not None else base_types.UninitialisedField(self, 'Cxl', CardPaymentDataSetTransaction50, False)

	@Cxl.deleter
	def Cxl(self):
		del self._Cxl
		self._Cxl = base_types.UninitialisedField(self, 'Cxl', CardPaymentDataSetTransaction50, False)

	@property
	def TknReq(self):
		return self._TknReq

	@TknReq.setter
	def TknReq(self, value):
		self._TknReq = value if value is not None else base_types.UninitialisedField(self, 'TknReq', TokenRequestComponent5, False)

	@TknReq.deleter
	def TknReq(self):
		del self._TknReq
		self._TknReq = base_types.UninitialisedField(self, 'TknReq', TokenRequestComponent5, False)

	@property
	def TknRspn(self):
		return self._TknRspn

	@TknRspn.setter
	def TknRspn(self, value):
		self._TknRspn = value if value is not None else base_types.UninitialisedField(self, 'TknRspn', TokenRequestComponent5, False)

	@TknRspn.deleter
	def TknRspn(self):
		del self._TknRspn
		self._TknRspn = base_types.UninitialisedField(self, 'TknRspn', TokenRequestComponent5, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AuthstnReq', type=CardPaymentDataSetTransaction52, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AuthstnRspn', type=CardPaymentDataSetTransaction53, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Cmpltn', type=CardPaymentDataSetTransaction51, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Cxl', type=CardPaymentDataSetTransaction50, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TknReq', type=TokenRequestComponent5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TknRspn', type=TokenRequestComponent5, min=0, max=1, mutex_group=1, array=False),
	))