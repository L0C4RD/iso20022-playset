import base_types
import CorporateActionProcessingStatus5Choice
import YesNoIndicator

class CorporateActionProcessingStatus7Choice(base_types._BaseFieldType):

	__slots__ = ["_ForInfOnly", "_EvtInfSts"]
	@property
	def ForInfOnly(self):
		return self._ForInfOnly

	@ForInfOnly.setter
	def ForInfOnly(self, value):
		self._ForInfOnly = value if type(value) != auto else self.make_default("ForInfOnly")

	@ForInfOnly.deleter
	def ForInfOnly(self):
		del self._ForInfOnly
		self._ForInfOnly = None

	@property
	def EvtInfSts(self):
		return self._EvtInfSts

	@EvtInfSts.setter
	def EvtInfSts(self, value):
		self._EvtInfSts = value if type(value) != auto else self.make_default("EvtInfSts")

	@EvtInfSts.deleter
	def EvtInfSts(self):
		del self._EvtInfSts
		self._EvtInfSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ForInfOnly', type=YesNoIndicator, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='EvtInfSts', type=CorporateActionProcessingStatus5Choice, min=0, max=1, mutex_group=1, array=False),
	))

