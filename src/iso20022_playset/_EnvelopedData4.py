# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import EncryptedContent3
from . import Number
from . import Recipient4Choice

class EnvelopedData4(base_types._BaseFieldType):

	__slots__ = ["_NcrptdCntt", "_Rcpt", "_Vrsn"]
	@property
	def NcrptdCntt(self):
		return self._NcrptdCntt

	@NcrptdCntt.setter
	def NcrptdCntt(self, value):
		self._NcrptdCntt = value if value is not None else base_types.UninitialisedField(self, 'NcrptdCntt', EncryptedContent3, False)

	@NcrptdCntt.deleter
	def NcrptdCntt(self):
		del self._NcrptdCntt
		self._NcrptdCntt = base_types.UninitialisedField(self, 'NcrptdCntt', EncryptedContent3, False)

	@property
	def Rcpt(self):
		return self._Rcpt

	@Rcpt.setter
	def Rcpt(self, value):
		self._Rcpt = value if value is not None else base_types.UninitialisedField(self, 'Rcpt', Recipient4Choice, True)

	@Rcpt.deleter
	def Rcpt(self):
		del self._Rcpt
		self._Rcpt = base_types.UninitialisedField(self, 'Rcpt', Recipient4Choice, True)

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
		base_types.FieldEntry(name='NcrptdCntt', type=EncryptedContent3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcpt', type=Recipient4Choice, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Vrsn', type=Number, min=0, max=1, mutex_group=None, array=False),
	))