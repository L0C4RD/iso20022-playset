# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AlgorithmIdentification16
from . import AlgorithmIdentification17
from . import Max3000Binary
from . import Number
from . import Recipient5Choice

class Signer3(base_types._BaseFieldType):

	__slots__ = ["_DgstAlgo", "_SgnrId", "_Sgntr", "_SgntrAlgo", "_Vrsn"]
	@property
	def DgstAlgo(self):
		return self._DgstAlgo

	@DgstAlgo.setter
	def DgstAlgo(self, value):
		self._DgstAlgo = value if value is not None else base_types.UninitialisedField(self, 'DgstAlgo', AlgorithmIdentification16, False)

	@DgstAlgo.deleter
	def DgstAlgo(self):
		del self._DgstAlgo
		self._DgstAlgo = base_types.UninitialisedField(self, 'DgstAlgo', AlgorithmIdentification16, False)

	@property
	def SgnrId(self):
		return self._SgnrId

	@SgnrId.setter
	def SgnrId(self, value):
		self._SgnrId = value if value is not None else base_types.UninitialisedField(self, 'SgnrId', Recipient5Choice, False)

	@SgnrId.deleter
	def SgnrId(self):
		del self._SgnrId
		self._SgnrId = base_types.UninitialisedField(self, 'SgnrId', Recipient5Choice, False)

	@property
	def Sgntr(self):
		return self._Sgntr

	@Sgntr.setter
	def Sgntr(self, value):
		self._Sgntr = value if value is not None else base_types.UninitialisedField(self, 'Sgntr', Max3000Binary, False)

	@Sgntr.deleter
	def Sgntr(self):
		del self._Sgntr
		self._Sgntr = base_types.UninitialisedField(self, 'Sgntr', Max3000Binary, False)

	@property
	def SgntrAlgo(self):
		return self._SgntrAlgo

	@SgntrAlgo.setter
	def SgntrAlgo(self, value):
		self._SgntrAlgo = value if value is not None else base_types.UninitialisedField(self, 'SgntrAlgo', AlgorithmIdentification17, False)

	@SgntrAlgo.deleter
	def SgntrAlgo(self):
		del self._SgntrAlgo
		self._SgntrAlgo = base_types.UninitialisedField(self, 'SgntrAlgo', AlgorithmIdentification17, False)

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
		base_types.FieldEntry(name='DgstAlgo', type=AlgorithmIdentification16, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SgnrId', type=Recipient5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sgntr', type=Max3000Binary, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SgntrAlgo', type=AlgorithmIdentification17, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vrsn', type=Number, min=0, max=1, mutex_group=None, array=False),
	))