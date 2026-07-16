# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import LEIIdentifier

class BondDerivative2(base_types._BaseFieldType):

	__slots__ = ["_IssncDt", "_Issr", "_MtrtyDt"]
	@property
	def IssncDt(self):
		return self._IssncDt

	@IssncDt.setter
	def IssncDt(self, value):
		self._IssncDt = value if value is not None else base_types.UninitialisedField(self, 'IssncDt', ISODate, False)

	@IssncDt.deleter
	def IssncDt(self):
		del self._IssncDt
		self._IssncDt = base_types.UninitialisedField(self, 'IssncDt', ISODate, False)

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if value is not None else base_types.UninitialisedField(self, 'Issr', LEIIdentifier, False)

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = base_types.UninitialisedField(self, 'Issr', LEIIdentifier, False)

	@property
	def MtrtyDt(self):
		return self._MtrtyDt

	@MtrtyDt.setter
	def MtrtyDt(self, value):
		self._MtrtyDt = value if value is not None else base_types.UninitialisedField(self, 'MtrtyDt', ISODate, False)

	@MtrtyDt.deleter
	def MtrtyDt(self):
		del self._MtrtyDt
		self._MtrtyDt = base_types.UninitialisedField(self, 'MtrtyDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='IssncDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=LEIIdentifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtrtyDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))