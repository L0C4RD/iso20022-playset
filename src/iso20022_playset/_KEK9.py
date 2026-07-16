# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AlgorithmIdentification32
from . import KEKIdentifier7
from . import Max500Binary
from . import Number

class KEK9(base_types._BaseFieldType):

	__slots__ = ["_KEKId", "_KeyNcrptnAlgo", "_NcrptdKey", "_Vrsn"]
	@property
	def KEKId(self):
		return self._KEKId

	@KEKId.setter
	def KEKId(self, value):
		self._KEKId = value if value is not None else base_types.UninitialisedField(self, 'KEKId', KEKIdentifier7, False)

	@KEKId.deleter
	def KEKId(self):
		del self._KEKId
		self._KEKId = base_types.UninitialisedField(self, 'KEKId', KEKIdentifier7, False)

	@property
	def KeyNcrptnAlgo(self):
		return self._KeyNcrptnAlgo

	@KeyNcrptnAlgo.setter
	def KeyNcrptnAlgo(self, value):
		self._KeyNcrptnAlgo = value if value is not None else base_types.UninitialisedField(self, 'KeyNcrptnAlgo', AlgorithmIdentification32, False)

	@KeyNcrptnAlgo.deleter
	def KeyNcrptnAlgo(self):
		del self._KeyNcrptnAlgo
		self._KeyNcrptnAlgo = base_types.UninitialisedField(self, 'KeyNcrptnAlgo', AlgorithmIdentification32, False)

	@property
	def NcrptdKey(self):
		return self._NcrptdKey

	@NcrptdKey.setter
	def NcrptdKey(self, value):
		self._NcrptdKey = value if value is not None else base_types.UninitialisedField(self, 'NcrptdKey', Max500Binary, False)

	@NcrptdKey.deleter
	def NcrptdKey(self):
		del self._NcrptdKey
		self._NcrptdKey = base_types.UninitialisedField(self, 'NcrptdKey', Max500Binary, False)

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
		base_types.FieldEntry(name='KEKId', type=KEKIdentifier7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='KeyNcrptnAlgo', type=AlgorithmIdentification32, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NcrptdKey', type=Max500Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vrsn', type=Number, min=0, max=1, mutex_group=None, array=False),
	))