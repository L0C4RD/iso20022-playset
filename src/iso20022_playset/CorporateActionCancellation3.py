import base_types
import Max140Text
import CorporateActionEventStatus1
import CorporateActionCancellationReason1Code

class CorporateActionCancellation3(base_types._BaseFieldType):

	__slots__ = ["_CxlRsn", "_CxlRsnCd", "_PrcgSts"]
	@property
	def CxlRsn(self):
		return self._CxlRsn

	@CxlRsn.setter
	def CxlRsn(self, value):
		self._CxlRsn = value if type(value) != auto else self.make_default("CxlRsn")

	@CxlRsn.deleter
	def CxlRsn(self):
		del self._CxlRsn
		self._CxlRsn = None

	@property
	def CxlRsnCd(self):
		return self._CxlRsnCd

	@CxlRsnCd.setter
	def CxlRsnCd(self, value):
		self._CxlRsnCd = value if type(value) != auto else self.make_default("CxlRsnCd")

	@CxlRsnCd.deleter
	def CxlRsnCd(self):
		del self._CxlRsnCd
		self._CxlRsnCd = None

	@property
	def PrcgSts(self):
		return self._PrcgSts

	@PrcgSts.setter
	def PrcgSts(self, value):
		self._PrcgSts = value if type(value) != auto else self.make_default("PrcgSts")

	@PrcgSts.deleter
	def PrcgSts(self):
		del self._PrcgSts
		self._PrcgSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CxlRsn', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlRsnCd', type=CorporateActionCancellationReason1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgSts', type=CorporateActionEventStatus1, min=1, max=1, mutex_group=None, array=False),
	))

