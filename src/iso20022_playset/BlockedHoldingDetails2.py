import base_types
import Max35Text
import DecimalNumber
import Holding1Code

class BlockedHoldingDetails2(base_types._BaseFieldType):

	__slots__ = ["_PrtlHldgUnits", "_HldgCertNb", "_BlckdHldg"]
	@property
	def PrtlHldgUnits(self):
		return self._PrtlHldgUnits

	@PrtlHldgUnits.setter
	def PrtlHldgUnits(self, value):
		self._PrtlHldgUnits = value if type(value) != auto else self.make_default("PrtlHldgUnits")

	@PrtlHldgUnits.deleter
	def PrtlHldgUnits(self):
		del self._PrtlHldgUnits
		self._PrtlHldgUnits = None

	@property
	def HldgCertNb(self):
		return self._HldgCertNb

	@HldgCertNb.setter
	def HldgCertNb(self, value):
		self._HldgCertNb = value if type(value) != auto else self.make_default("HldgCertNb")

	@HldgCertNb.deleter
	def HldgCertNb(self):
		del self._HldgCertNb
		self._HldgCertNb = None

	@property
	def BlckdHldg(self):
		return self._BlckdHldg

	@BlckdHldg.setter
	def BlckdHldg(self, value):
		self._BlckdHldg = value if type(value) != auto else self.make_default("BlckdHldg")

	@BlckdHldg.deleter
	def BlckdHldg(self):
		del self._BlckdHldg
		self._BlckdHldg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrtlHldgUnits', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HldgCertNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckdHldg', type=Holding1Code, min=1, max=1, mutex_group=None, array=False),
	))

