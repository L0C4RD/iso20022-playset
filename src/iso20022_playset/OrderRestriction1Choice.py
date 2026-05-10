import base_types
import GenericIdentification30
import OrderRestrictionType1Code

class OrderRestriction1Choice(base_types._BaseFieldType):

	__slots__ = ["_OrdrRstrctnCd", "_Prtry"]
	@property
	def OrdrRstrctnCd(self):
		return self._OrdrRstrctnCd

	@OrdrRstrctnCd.setter
	def OrdrRstrctnCd(self, value):
		self._OrdrRstrctnCd = value if type(value) != auto else self.make_default("OrdrRstrctnCd")

	@OrdrRstrctnCd.deleter
	def OrdrRstrctnCd(self):
		del self._OrdrRstrctnCd
		self._OrdrRstrctnCd = None

	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if type(value) != auto else self.make_default("Prtry")

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrdrRstrctnCd', type=OrderRestrictionType1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=GenericIdentification30, min=0, max=1, mutex_group=1, array=False),
	))

