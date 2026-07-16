# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Algorithm13Code
from . import Algorithm15Code
from . import Algorithm7Code
from . import EncryptionFormat1Code
from . import TrueFalseIndicator

class ATMSecurityConfiguration3(base_types._BaseFieldType):

	__slots__ = ["_AsmmtrcKeyStdId", "_AsmmtrcNcrptn", "_AsmmtrcNcrptnAlgo", "_NcrptnFrmt", "_SmmtrcNcrptnAlgo", "_SmmtrcTrnsprtKey", "_SmmtrcTrnsprtKeyAlgo"]
	@property
	def AsmmtrcKeyStdId(self):
		return self._AsmmtrcKeyStdId

	@AsmmtrcKeyStdId.setter
	def AsmmtrcKeyStdId(self, value):
		self._AsmmtrcKeyStdId = value if value is not None else base_types.UninitialisedField(self, 'AsmmtrcKeyStdId', TrueFalseIndicator, False)

	@AsmmtrcKeyStdId.deleter
	def AsmmtrcKeyStdId(self):
		del self._AsmmtrcKeyStdId
		self._AsmmtrcKeyStdId = base_types.UninitialisedField(self, 'AsmmtrcKeyStdId', TrueFalseIndicator, False)

	@property
	def AsmmtrcNcrptn(self):
		return self._AsmmtrcNcrptn

	@AsmmtrcNcrptn.setter
	def AsmmtrcNcrptn(self, value):
		self._AsmmtrcNcrptn = value if value is not None else base_types.UninitialisedField(self, 'AsmmtrcNcrptn', TrueFalseIndicator, False)

	@AsmmtrcNcrptn.deleter
	def AsmmtrcNcrptn(self):
		del self._AsmmtrcNcrptn
		self._AsmmtrcNcrptn = base_types.UninitialisedField(self, 'AsmmtrcNcrptn', TrueFalseIndicator, False)

	@property
	def AsmmtrcNcrptnAlgo(self):
		return self._AsmmtrcNcrptnAlgo

	@AsmmtrcNcrptnAlgo.setter
	def AsmmtrcNcrptnAlgo(self, value):
		self._AsmmtrcNcrptnAlgo = value if value is not None else base_types.UninitialisedField(self, 'AsmmtrcNcrptnAlgo', Algorithm7Code, True)

	@AsmmtrcNcrptnAlgo.deleter
	def AsmmtrcNcrptnAlgo(self):
		del self._AsmmtrcNcrptnAlgo
		self._AsmmtrcNcrptnAlgo = base_types.UninitialisedField(self, 'AsmmtrcNcrptnAlgo', Algorithm7Code, True)

	@property
	def NcrptnFrmt(self):
		return self._NcrptnFrmt

	@NcrptnFrmt.setter
	def NcrptnFrmt(self, value):
		self._NcrptnFrmt = value if value is not None else base_types.UninitialisedField(self, 'NcrptnFrmt', EncryptionFormat1Code, True)

	@NcrptnFrmt.deleter
	def NcrptnFrmt(self):
		del self._NcrptnFrmt
		self._NcrptnFrmt = base_types.UninitialisedField(self, 'NcrptnFrmt', EncryptionFormat1Code, True)

	@property
	def SmmtrcNcrptnAlgo(self):
		return self._SmmtrcNcrptnAlgo

	@SmmtrcNcrptnAlgo.setter
	def SmmtrcNcrptnAlgo(self, value):
		self._SmmtrcNcrptnAlgo = value if value is not None else base_types.UninitialisedField(self, 'SmmtrcNcrptnAlgo', Algorithm15Code, True)

	@SmmtrcNcrptnAlgo.deleter
	def SmmtrcNcrptnAlgo(self):
		del self._SmmtrcNcrptnAlgo
		self._SmmtrcNcrptnAlgo = base_types.UninitialisedField(self, 'SmmtrcNcrptnAlgo', Algorithm15Code, True)

	@property
	def SmmtrcTrnsprtKey(self):
		return self._SmmtrcTrnsprtKey

	@SmmtrcTrnsprtKey.setter
	def SmmtrcTrnsprtKey(self, value):
		self._SmmtrcTrnsprtKey = value if value is not None else base_types.UninitialisedField(self, 'SmmtrcTrnsprtKey', TrueFalseIndicator, False)

	@SmmtrcTrnsprtKey.deleter
	def SmmtrcTrnsprtKey(self):
		del self._SmmtrcTrnsprtKey
		self._SmmtrcTrnsprtKey = base_types.UninitialisedField(self, 'SmmtrcTrnsprtKey', TrueFalseIndicator, False)

	@property
	def SmmtrcTrnsprtKeyAlgo(self):
		return self._SmmtrcTrnsprtKeyAlgo

	@SmmtrcTrnsprtKeyAlgo.setter
	def SmmtrcTrnsprtKeyAlgo(self, value):
		self._SmmtrcTrnsprtKeyAlgo = value if value is not None else base_types.UninitialisedField(self, 'SmmtrcTrnsprtKeyAlgo', Algorithm13Code, True)

	@SmmtrcTrnsprtKeyAlgo.deleter
	def SmmtrcTrnsprtKeyAlgo(self):
		del self._SmmtrcTrnsprtKeyAlgo
		self._SmmtrcTrnsprtKeyAlgo = base_types.UninitialisedField(self, 'SmmtrcTrnsprtKeyAlgo', Algorithm13Code, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AsmmtrcKeyStdId', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AsmmtrcNcrptn', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AsmmtrcNcrptnAlgo', type=Algorithm7Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NcrptnFrmt', type=EncryptionFormat1Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SmmtrcNcrptnAlgo', type=Algorithm15Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SmmtrcTrnsprtKey', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SmmtrcTrnsprtKeyAlgo', type=Algorithm13Code, min=0, max=None, mutex_group=None, array=True),
	))