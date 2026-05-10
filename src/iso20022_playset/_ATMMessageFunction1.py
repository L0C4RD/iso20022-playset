from . import base_types
from .Max35Text import Max35Text
from .MessageFunction7Code import MessageFunction7Code

class ATMMessageFunction1(base_types._BaseFieldType):

	__slots__ = ["_Fctn", "_ATMSvcCd", "_HstSvcCd"]
	@property
	def Fctn(self):
		return self._Fctn

	@Fctn.setter
	def Fctn(self, value):
		self._Fctn = value if type(value) != base_types.auto else self.make_default("Fctn")

	@Fctn.deleter
	def Fctn(self):
		del self._Fctn
		self._Fctn = None

	@property
	def ATMSvcCd(self):
		return self._ATMSvcCd

	@ATMSvcCd.setter
	def ATMSvcCd(self, value):
		self._ATMSvcCd = value if type(value) != base_types.auto else self.make_default("ATMSvcCd")

	@ATMSvcCd.deleter
	def ATMSvcCd(self):
		del self._ATMSvcCd
		self._ATMSvcCd = None

	@property
	def HstSvcCd(self):
		return self._HstSvcCd

	@HstSvcCd.setter
	def HstSvcCd(self, value):
		self._HstSvcCd = value if type(value) != base_types.auto else self.make_default("HstSvcCd")

	@HstSvcCd.deleter
	def HstSvcCd(self):
		del self._HstSvcCd
		self._HstSvcCd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Fctn', type=MessageFunction7Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ATMSvcCd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HstSvcCd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

