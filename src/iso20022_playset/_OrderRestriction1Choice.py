# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericIdentification30
from . import OrderRestrictionType1Code

class OrderRestriction1Choice(base_types._BaseFieldType):

	__slots__ = ["_OrdrRstrctnCd", "_Prtry"]
	@property
	def OrdrRstrctnCd(self):
		return self._OrdrRstrctnCd

	@OrdrRstrctnCd.setter
	def OrdrRstrctnCd(self, value):
		self._OrdrRstrctnCd = value if value is not None else base_types.UninitialisedField(self, 'OrdrRstrctnCd', OrderRestrictionType1Code, False)

	@OrdrRstrctnCd.deleter
	def OrdrRstrctnCd(self):
		del self._OrdrRstrctnCd
		self._OrdrRstrctnCd = base_types.UninitialisedField(self, 'OrdrRstrctnCd', OrderRestrictionType1Code, False)

	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if value is not None else base_types.UninitialisedField(self, 'Prtry', GenericIdentification30, False)

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = base_types.UninitialisedField(self, 'Prtry', GenericIdentification30, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrdrRstrctnCd', type=OrderRestrictionType1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=GenericIdentification30, min=0, max=1, mutex_group=1, array=False),
	))