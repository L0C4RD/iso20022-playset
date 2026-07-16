# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMServiceType12Code
from . import Max35Text

class ATMService26(base_types._BaseFieldType):

	__slots__ = ["_ATMSvcCd", "_HstSvcCd", "_SvcRef", "_SvcTp", "_SvcVarntId"]
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
	def HstSvcCd(self):
		return self._HstSvcCd

	@HstSvcCd.setter
	def HstSvcCd(self, value):
		self._HstSvcCd = value if value is not None else base_types.UninitialisedField(self, 'HstSvcCd', Max35Text, False)

	@HstSvcCd.deleter
	def HstSvcCd(self):
		del self._HstSvcCd
		self._HstSvcCd = base_types.UninitialisedField(self, 'HstSvcCd', Max35Text, False)

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
		self._SvcTp = value if value is not None else base_types.UninitialisedField(self, 'SvcTp', ATMServiceType12Code, False)

	@SvcTp.deleter
	def SvcTp(self):
		del self._SvcTp
		self._SvcTp = base_types.UninitialisedField(self, 'SvcTp', ATMServiceType12Code, False)

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
		base_types.FieldEntry(name='HstSvcCd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcTp', type=ATMServiceType12Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcVarntId', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
	))