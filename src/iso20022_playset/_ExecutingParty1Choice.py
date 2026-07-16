# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max50Text
from . import NoReasonCode
from . import PersonIdentification12

class ExecutingParty1Choice(base_types._BaseFieldType):

	__slots__ = ["_Algo", "_Clnt", "_Prsn"]
	@property
	def Algo(self):
		return self._Algo

	@Algo.setter
	def Algo(self, value):
		self._Algo = value if value is not None else base_types.UninitialisedField(self, 'Algo', Max50Text, False)

	@Algo.deleter
	def Algo(self):
		del self._Algo
		self._Algo = base_types.UninitialisedField(self, 'Algo', Max50Text, False)

	@property
	def Clnt(self):
		return self._Clnt

	@Clnt.setter
	def Clnt(self, value):
		self._Clnt = value if value is not None else base_types.UninitialisedField(self, 'Clnt', NoReasonCode, False)

	@Clnt.deleter
	def Clnt(self):
		del self._Clnt
		self._Clnt = base_types.UninitialisedField(self, 'Clnt', NoReasonCode, False)

	@property
	def Prsn(self):
		return self._Prsn

	@Prsn.setter
	def Prsn(self, value):
		self._Prsn = value if value is not None else base_types.UninitialisedField(self, 'Prsn', PersonIdentification12, False)

	@Prsn.deleter
	def Prsn(self):
		del self._Prsn
		self._Prsn = base_types.UninitialisedField(self, 'Prsn', PersonIdentification12, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Algo', type=Max50Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Clnt', type=NoReasonCode, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prsn', type=PersonIdentification12, min=0, max=1, mutex_group=1, array=False),
	))