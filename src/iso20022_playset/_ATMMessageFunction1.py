# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Max35Text import Max35Text
from ._MessageFunction7Code import MessageFunction7Code

class ATMMessageFunction1(base_types._BaseFieldType):

	__slots__ = ["_ATMSvcCd", "_Fctn", "_HstSvcCd"]
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
		base_types.FieldEntry(name='ATMSvcCd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Fctn', type=MessageFunction7Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HstSvcCd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))