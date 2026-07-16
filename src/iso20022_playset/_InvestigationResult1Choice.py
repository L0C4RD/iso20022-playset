# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InvestigationStatus1Code
from . import SupplementaryDataEnvelope1

class InvestigationResult1Choice(base_types._BaseFieldType):

	__slots__ = ["_InvstgtnSts", "_Rslt"]
	@property
	def InvstgtnSts(self):
		return self._InvstgtnSts

	@InvstgtnSts.setter
	def InvstgtnSts(self, value):
		self._InvstgtnSts = value if value is not None else base_types.UninitialisedField(self, 'InvstgtnSts', InvestigationStatus1Code, False)

	@InvstgtnSts.deleter
	def InvstgtnSts(self):
		del self._InvstgtnSts
		self._InvstgtnSts = base_types.UninitialisedField(self, 'InvstgtnSts', InvestigationStatus1Code, False)

	@property
	def Rslt(self):
		return self._Rslt

	@Rslt.setter
	def Rslt(self, value):
		self._Rslt = value if value is not None else base_types.UninitialisedField(self, 'Rslt', SupplementaryDataEnvelope1, False)

	@Rslt.deleter
	def Rslt(self):
		del self._Rslt
		self._Rslt = base_types.UninitialisedField(self, 'Rslt', SupplementaryDataEnvelope1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='InvstgtnSts', type=InvestigationStatus1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rslt', type=SupplementaryDataEnvelope1, min=0, max=1, mutex_group=1, array=False),
	))