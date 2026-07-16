# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ProprietaryReason4
from . import ProprietaryStatusAndReason6

class AllocationStatus1Choice(base_types._BaseFieldType):

	__slots__ = ["_FullyAllctd", "_PrtlyAllctd", "_Prtry"]
	@property
	def FullyAllctd(self):
		return self._FullyAllctd

	@FullyAllctd.setter
	def FullyAllctd(self, value):
		self._FullyAllctd = value if value is not None else base_types.UninitialisedField(self, 'FullyAllctd', ProprietaryReason4, False)

	@FullyAllctd.deleter
	def FullyAllctd(self):
		del self._FullyAllctd
		self._FullyAllctd = base_types.UninitialisedField(self, 'FullyAllctd', ProprietaryReason4, False)

	@property
	def PrtlyAllctd(self):
		return self._PrtlyAllctd

	@PrtlyAllctd.setter
	def PrtlyAllctd(self, value):
		self._PrtlyAllctd = value if value is not None else base_types.UninitialisedField(self, 'PrtlyAllctd', ProprietaryReason4, False)

	@PrtlyAllctd.deleter
	def PrtlyAllctd(self):
		del self._PrtlyAllctd
		self._PrtlyAllctd = base_types.UninitialisedField(self, 'PrtlyAllctd', ProprietaryReason4, False)

	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if value is not None else base_types.UninitialisedField(self, 'Prtry', ProprietaryStatusAndReason6, False)

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = base_types.UninitialisedField(self, 'Prtry', ProprietaryStatusAndReason6, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FullyAllctd', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtlyAllctd', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=ProprietaryStatusAndReason6, min=0, max=1, mutex_group=1, array=False),
	))