# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AlgorithmIdentification27
from . import Max5000Binary
from . import Number
from . import Recipient5Choice

class KeyTransport6(base_types._BaseFieldType):

	__slots__ = ["_KeyNcrptnAlgo", "_NcrptdKey", "_RcptId", "_Vrsn"]
	@property
	def KeyNcrptnAlgo(self):
		return self._KeyNcrptnAlgo

	@KeyNcrptnAlgo.setter
	def KeyNcrptnAlgo(self, value):
		self._KeyNcrptnAlgo = value if value is not None else base_types.UninitialisedField(self, 'KeyNcrptnAlgo', AlgorithmIdentification27, False)

	@KeyNcrptnAlgo.deleter
	def KeyNcrptnAlgo(self):
		del self._KeyNcrptnAlgo
		self._KeyNcrptnAlgo = base_types.UninitialisedField(self, 'KeyNcrptnAlgo', AlgorithmIdentification27, False)

	@property
	def NcrptdKey(self):
		return self._NcrptdKey

	@NcrptdKey.setter
	def NcrptdKey(self, value):
		self._NcrptdKey = value if value is not None else base_types.UninitialisedField(self, 'NcrptdKey', Max5000Binary, False)

	@NcrptdKey.deleter
	def NcrptdKey(self):
		del self._NcrptdKey
		self._NcrptdKey = base_types.UninitialisedField(self, 'NcrptdKey', Max5000Binary, False)

	@property
	def RcptId(self):
		return self._RcptId

	@RcptId.setter
	def RcptId(self, value):
		self._RcptId = value if value is not None else base_types.UninitialisedField(self, 'RcptId', Recipient5Choice, False)

	@RcptId.deleter
	def RcptId(self):
		del self._RcptId
		self._RcptId = base_types.UninitialisedField(self, 'RcptId', Recipient5Choice, False)

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
		base_types.FieldEntry(name='KeyNcrptnAlgo', type=AlgorithmIdentification27, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NcrptdKey', type=Max5000Binary, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcptId', type=Recipient5Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vrsn', type=Number, min=0, max=1, mutex_group=None, array=False),
	))