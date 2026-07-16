# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMServiceType6Code
from . import Max35Text
from . import TrueFalseIndicator

class ATMService11(base_types._BaseFieldType):

	__slots__ = ["_ATMSvcCd", "_CshBck", "_MultiAcct", "_SvcRef", "_SvcTp", "_SvcVarntId"]
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
	def CshBck(self):
		return self._CshBck

	@CshBck.setter
	def CshBck(self, value):
		self._CshBck = value if value is not None else base_types.UninitialisedField(self, 'CshBck', TrueFalseIndicator, False)

	@CshBck.deleter
	def CshBck(self):
		del self._CshBck
		self._CshBck = base_types.UninitialisedField(self, 'CshBck', TrueFalseIndicator, False)

	@property
	def MultiAcct(self):
		return self._MultiAcct

	@MultiAcct.setter
	def MultiAcct(self, value):
		self._MultiAcct = value if value is not None else base_types.UninitialisedField(self, 'MultiAcct', TrueFalseIndicator, False)

	@MultiAcct.deleter
	def MultiAcct(self):
		del self._MultiAcct
		self._MultiAcct = base_types.UninitialisedField(self, 'MultiAcct', TrueFalseIndicator, False)

	@property
	def SvcRef(self):
		return self._SvcRef

	@SvcRef.setter
	def SvcRef(self, value):
		self._SvcRef = value if value is not None else base_types.UninitialisedField(self, 'SvcRef', Max35Text, False)

	@SvcRef.deleter
	def SvcRef(self):
		del self._SvcRef
		self._SvcRef = base_types.UninitialisedField(self, 'SvcRef', Max35Text, False)

	@property
	def SvcTp(self):
		return self._SvcTp

	@SvcTp.setter
	def SvcTp(self, value):
		self._SvcTp = value if value is not None else base_types.UninitialisedField(self, 'SvcTp', ATMServiceType6Code, False)

	@SvcTp.deleter
	def SvcTp(self):
		del self._SvcTp
		self._SvcTp = base_types.UninitialisedField(self, 'SvcTp', ATMServiceType6Code, False)

	@property
	def SvcVarntId(self):
		return self._SvcVarntId

	@SvcVarntId.setter
	def SvcVarntId(self, value):
		self._SvcVarntId = value if value is not None else base_types.UninitialisedField(self, 'SvcVarntId', Max35Text, True)

	@SvcVarntId.deleter
	def SvcVarntId(self):
		del self._SvcVarntId
		self._SvcVarntId = base_types.UninitialisedField(self, 'SvcVarntId', Max35Text, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ATMSvcCd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshBck', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MultiAcct', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcTp', type=ATMServiceType6Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcVarntId', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
	))