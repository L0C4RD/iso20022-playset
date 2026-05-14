# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CardPaymentDataSetTransaction54 import CardPaymentDataSetTransaction54
from ._CardPaymentDataSetTransaction55 import CardPaymentDataSetTransaction55
from ._CardPaymentDataSetTransaction56 import CardPaymentDataSetTransaction56
from ._CardPaymentDataSetTransaction57 import CardPaymentDataSetTransaction57
from ._TokenRequestComponent6 import TokenRequestComponent6

class CardPaymentDataSetTransaction14Choice(base_types._BaseFieldType):

	__slots__ = ["_AuthstnReq", "_AuthstnRspn", "_Cmpltn", "_Cxl", "_TknReq", "_TknRspn"]
	@property
	def AuthstnReq(self):
		return self._AuthstnReq

	@AuthstnReq.setter
	def AuthstnReq(self, value):
		self._AuthstnReq = value if type(value) != base_types.auto else self.make_default("AuthstnReq")

	@AuthstnReq.deleter
	def AuthstnReq(self):
		del self._AuthstnReq
		self._AuthstnReq = None

	@property
	def AuthstnRspn(self):
		return self._AuthstnRspn

	@AuthstnRspn.setter
	def AuthstnRspn(self, value):
		self._AuthstnRspn = value if type(value) != base_types.auto else self.make_default("AuthstnRspn")

	@AuthstnRspn.deleter
	def AuthstnRspn(self):
		del self._AuthstnRspn
		self._AuthstnRspn = None

	@property
	def Cmpltn(self):
		return self._Cmpltn

	@Cmpltn.setter
	def Cmpltn(self, value):
		self._Cmpltn = value if type(value) != base_types.auto else self.make_default("Cmpltn")

	@Cmpltn.deleter
	def Cmpltn(self):
		del self._Cmpltn
		self._Cmpltn = None

	@property
	def Cxl(self):
		return self._Cxl

	@Cxl.setter
	def Cxl(self, value):
		self._Cxl = value if type(value) != base_types.auto else self.make_default("Cxl")

	@Cxl.deleter
	def Cxl(self):
		del self._Cxl
		self._Cxl = None

	@property
	def TknReq(self):
		return self._TknReq

	@TknReq.setter
	def TknReq(self, value):
		self._TknReq = value if type(value) != base_types.auto else self.make_default("TknReq")

	@TknReq.deleter
	def TknReq(self):
		del self._TknReq
		self._TknReq = None

	@property
	def TknRspn(self):
		return self._TknRspn

	@TknRspn.setter
	def TknRspn(self, value):
		self._TknRspn = value if type(value) != base_types.auto else self.make_default("TknRspn")

	@TknRspn.deleter
	def TknRspn(self):
		del self._TknRspn
		self._TknRspn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AuthstnReq', type=CardPaymentDataSetTransaction56, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AuthstnRspn', type=CardPaymentDataSetTransaction57, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Cmpltn', type=CardPaymentDataSetTransaction55, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Cxl', type=CardPaymentDataSetTransaction54, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TknReq', type=TokenRequestComponent6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TknRspn', type=TokenRequestComponent6, min=0, max=1, mutex_group=1, array=False),
	))