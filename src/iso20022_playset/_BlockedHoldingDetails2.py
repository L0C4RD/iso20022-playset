# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DecimalNumber
from . import Holding1Code
from . import Max35Text

class BlockedHoldingDetails2(base_types._BaseFieldType):

	__slots__ = ["_BlckdHldg", "_HldgCertNb", "_PrtlHldgUnits"]
	@property
	def BlckdHldg(self):
		return self._BlckdHldg

	@BlckdHldg.setter
	def BlckdHldg(self, value):
		self._BlckdHldg = value if value is not None else base_types.UninitialisedField(self, 'BlckdHldg', Holding1Code, False)

	@BlckdHldg.deleter
	def BlckdHldg(self):
		del self._BlckdHldg
		self._BlckdHldg = base_types.UninitialisedField(self, 'BlckdHldg', Holding1Code, False)

	@property
	def HldgCertNb(self):
		return self._HldgCertNb

	@HldgCertNb.setter
	def HldgCertNb(self, value):
		self._HldgCertNb = value if value is not None else base_types.UninitialisedField(self, 'HldgCertNb', Max35Text, False)

	@HldgCertNb.deleter
	def HldgCertNb(self):
		del self._HldgCertNb
		self._HldgCertNb = base_types.UninitialisedField(self, 'HldgCertNb', Max35Text, False)

	@property
	def PrtlHldgUnits(self):
		return self._PrtlHldgUnits

	@PrtlHldgUnits.setter
	def PrtlHldgUnits(self, value):
		self._PrtlHldgUnits = value if value is not None else base_types.UninitialisedField(self, 'PrtlHldgUnits', DecimalNumber, False)

	@PrtlHldgUnits.deleter
	def PrtlHldgUnits(self):
		del self._PrtlHldgUnits
		self._PrtlHldgUnits = base_types.UninitialisedField(self, 'PrtlHldgUnits', DecimalNumber, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BlckdHldg', type=Holding1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HldgCertNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtlHldgUnits', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
	))