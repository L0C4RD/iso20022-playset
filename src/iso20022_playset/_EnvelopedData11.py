# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import EncryptedContent7
from . import Number
from . import OriginatorInformation1
from . import Recipient15Choice

class EnvelopedData11(base_types._BaseFieldType):

	__slots__ = ["_NcrptdCntt", "_OrgtrInf", "_Rcpt", "_Vrsn"]
	@property
	def NcrptdCntt(self):
		return self._NcrptdCntt

	@NcrptdCntt.setter
	def NcrptdCntt(self, value):
		self._NcrptdCntt = value if value is not None else base_types.UninitialisedField(self, 'NcrptdCntt', EncryptedContent7, False)

	@NcrptdCntt.deleter
	def NcrptdCntt(self):
		del self._NcrptdCntt
		self._NcrptdCntt = base_types.UninitialisedField(self, 'NcrptdCntt', EncryptedContent7, False)

	@property
	def OrgtrInf(self):
		return self._OrgtrInf

	@OrgtrInf.setter
	def OrgtrInf(self, value):
		self._OrgtrInf = value if value is not None else base_types.UninitialisedField(self, 'OrgtrInf', OriginatorInformation1, False)

	@OrgtrInf.deleter
	def OrgtrInf(self):
		del self._OrgtrInf
		self._OrgtrInf = base_types.UninitialisedField(self, 'OrgtrInf', OriginatorInformation1, False)

	@property
	def Rcpt(self):
		return self._Rcpt

	@Rcpt.setter
	def Rcpt(self, value):
		self._Rcpt = value if value is not None else base_types.UninitialisedField(self, 'Rcpt', Recipient15Choice, True)

	@Rcpt.deleter
	def Rcpt(self):
		del self._Rcpt
		self._Rcpt = base_types.UninitialisedField(self, 'Rcpt', Recipient15Choice, True)

	@property
	def Vrsn(self):
		return self._Vrsn

	@Vrsn.setter
	def Vrsn(self, value):
		self._Vrsn = value if value is not None else base_types.UninitialisedField(self, 'Vrsn', Number, False)

	@Vrsn.deleter
	def Vrsn(self):
		del self._Vrsn
		self._Vrsn = base_types.UninitialisedField(self, 'Vrsn', Number, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NcrptdCntt', type=EncryptedContent7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgtrInf', type=OriginatorInformation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcpt', type=Recipient15Choice, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Vrsn', type=Number, min=0, max=1, mutex_group=None, array=False),
	))