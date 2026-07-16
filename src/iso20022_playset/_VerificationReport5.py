# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import IdentificationInformation5
from . import IdentificationVerificationIndicator
from . import Max35Text
from . import VerificationReason1Choice

class VerificationReport5(base_types._BaseFieldType):

	__slots__ = ["_OrgnlId", "_OrgnlPtyAndAcctId", "_Rsn", "_UpdtdPtyAndAcctId", "_Vrfctn"]
	@property
	def OrgnlId(self):
		return self._OrgnlId

	@OrgnlId.setter
	def OrgnlId(self, value):
		self._OrgnlId = value if value is not None else base_types.UninitialisedField(self, 'OrgnlId', Max35Text, False)

	@OrgnlId.deleter
	def OrgnlId(self):
		del self._OrgnlId
		self._OrgnlId = base_types.UninitialisedField(self, 'OrgnlId', Max35Text, False)

	@property
	def OrgnlPtyAndAcctId(self):
		return self._OrgnlPtyAndAcctId

	@OrgnlPtyAndAcctId.setter
	def OrgnlPtyAndAcctId(self, value):
		self._OrgnlPtyAndAcctId = value if value is not None else base_types.UninitialisedField(self, 'OrgnlPtyAndAcctId', IdentificationInformation5, False)

	@OrgnlPtyAndAcctId.deleter
	def OrgnlPtyAndAcctId(self):
		del self._OrgnlPtyAndAcctId
		self._OrgnlPtyAndAcctId = base_types.UninitialisedField(self, 'OrgnlPtyAndAcctId', IdentificationInformation5, False)

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if value is not None else base_types.UninitialisedField(self, 'Rsn', VerificationReason1Choice, False)

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = base_types.UninitialisedField(self, 'Rsn', VerificationReason1Choice, False)

	@property
	def UpdtdPtyAndAcctId(self):
		return self._UpdtdPtyAndAcctId

	@UpdtdPtyAndAcctId.setter
	def UpdtdPtyAndAcctId(self, value):
		self._UpdtdPtyAndAcctId = value if value is not None else base_types.UninitialisedField(self, 'UpdtdPtyAndAcctId', IdentificationInformation5, False)

	@UpdtdPtyAndAcctId.deleter
	def UpdtdPtyAndAcctId(self):
		del self._UpdtdPtyAndAcctId
		self._UpdtdPtyAndAcctId = base_types.UninitialisedField(self, 'UpdtdPtyAndAcctId', IdentificationInformation5, False)

	@property
	def Vrfctn(self):
		return self._Vrfctn

	@Vrfctn.setter
	def Vrfctn(self, value):
		self._Vrfctn = value if value is not None else base_types.UninitialisedField(self, 'Vrfctn', IdentificationVerificationIndicator, False)

	@Vrfctn.deleter
	def Vrfctn(self):
		del self._Vrfctn
		self._Vrfctn = base_types.UninitialisedField(self, 'Vrfctn', IdentificationVerificationIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlPtyAndAcctId', type=IdentificationInformation5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsn', type=VerificationReason1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UpdtdPtyAndAcctId', type=IdentificationInformation5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vrfctn', type=IdentificationVerificationIndicator, min=1, max=1, mutex_group=None, array=False),
	))