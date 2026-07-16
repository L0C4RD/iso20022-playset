# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import MessageFunction7Code

class ATMMessageFunction1(base_types._BaseFieldType):

	__slots__ = ["_ATMSvcCd", "_Fctn", "_HstSvcCd"]
	@property
	def ATMSvcCd(self):
		return self._ATMSvcCd

	@ATMSvcCd.setter
	def ATMSvcCd(self, value):
		self._ATMSvcCd = value if value is not None else base_types.UninitialisedField(self, 'ATMSvcCd', Max35Text, False)

	@ATMSvcCd.deleter
	def ATMSvcCd(self):
		del self._ATMSvcCd
		self._ATMSvcCd = base_types.UninitialisedField(self, 'ATMSvcCd', Max35Text, False)

	@property
	def Fctn(self):
		return self._Fctn

	@Fctn.setter
	def Fctn(self, value):
		self._Fctn = value if value is not None else base_types.UninitialisedField(self, 'Fctn', MessageFunction7Code, False)

	@Fctn.deleter
	def Fctn(self):
		del self._Fctn
		self._Fctn = base_types.UninitialisedField(self, 'Fctn', MessageFunction7Code, False)

	@property
	def HstSvcCd(self):
		return self._HstSvcCd

	@HstSvcCd.setter
	def HstSvcCd(self, value):
		self._HstSvcCd = value if value is not None else base_types.UninitialisedField(self, 'HstSvcCd', Max35Text, False)

	@HstSvcCd.deleter
	def HstSvcCd(self):
		del self._HstSvcCd
		self._HstSvcCd = base_types.UninitialisedField(self, 'HstSvcCd', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ATMSvcCd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Fctn', type=MessageFunction7Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HstSvcCd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))